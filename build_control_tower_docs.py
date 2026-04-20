from __future__ import annotations

import argparse
import csv
import json
import re
from collections import OrderedDict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


REQUIRED_COLUMNS = {"id", "title", "group", "row_type", "one_liner", "context"}


@dataclass
class Project:
    id: str
    title: str
    group: str
    one_liner: str
    context: str


@dataclass
class Subgroup:
    id: str
    title: str
    one_liner: str
    context: str
    projects: list[Project] = field(default_factory=list)


@dataclass
class TopGroup:
    id: str
    title: str
    one_liner: str
    context: str
    subgroups: OrderedDict[str, Subgroup] = field(default_factory=OrderedDict)
    projects: list[Project] = field(default_factory=list)


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = text.replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-") or "untitled"


def md_escape(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n").strip()


def ensure_columns(fieldnames: Iterable[str] | None) -> None:
    actual = set(fieldnames or [])
    missing = REQUIRED_COLUMNS - actual
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def load_rows(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        ensure_columns(reader.fieldnames)
        rows = []
        for i, row in enumerate(reader, start=2):
            clean = {k: (v or "").strip() for k, v in row.items()}
            clean["__line__"] = str(i)
            rows.append(clean)
        return rows


def build_tree(rows: list[dict[str, str]]) -> OrderedDict[str, TopGroup]:
    top_groups: OrderedDict[str, TopGroup] = OrderedDict()
    current_top_id: str | None = None
    current_sub_id: str | None = None

    for row in rows:
        line = row["__line__"]
        row_type = row["row_type"].lower()
        item_id = row["id"]
        title = row["title"]
        group = row["group"]
        one_liner = row["one_liner"]
        context = row["context"]

        if row_type == "group":
            depth = item_id.count(".")
            if depth == 0:
                current_top_id = item_id
                current_sub_id = None
                if item_id in top_groups:
                    raise ValueError(f"Line {line}: duplicate top-level group id '{item_id}'")
                top_groups[item_id] = TopGroup(
                    id=item_id,
                    title=title,
                    one_liner=one_liner,
                    context=context,
                )
            elif depth == 1:
                parent_id = item_id.split(".")[0]
                if parent_id not in top_groups:
                    raise ValueError(
                        f"Line {line}: subgroup '{item_id}' references missing parent '{parent_id}'"
                    )
                current_top_id = parent_id
                current_sub_id = item_id
                parent = top_groups[parent_id]
                if item_id in parent.subgroups:
                    raise ValueError(f"Line {line}: duplicate subgroup id '{item_id}'")
                parent.subgroups[item_id] = Subgroup(
                    id=item_id,
                    title=title,
                    one_liner=one_liner,
                    context=context,
                )
            else:
                raise ValueError(
                    f"Line {line}: unsupported group nesting depth for id '{item_id}'"
                )

        elif row_type == "project":
            if not group:
                raise ValueError(f"Line {line}: project '{title}' is missing group")
            if group not in top_groups:
                raise ValueError(
                    f"Line {line}: project '{title}' references unknown top-level group '{group}'"
                )

            project = Project(
                id=item_id,
                title=title,
                group=group,
                one_liner=one_liner,
                context=context,
            )
            parent = top_groups[group]

            if current_top_id == group and current_sub_id and current_sub_id in parent.subgroups:
                parent.subgroups[current_sub_id].projects.append(project)
            else:
                parent.projects.append(project)
        else:
            raise ValueError(f"Line {line}: invalid row_type '{row_type}'")

    return top_groups


def render_project(project: Project, heading_level: int = 2) -> str:
    hashes = "#" * heading_level
    return (
        f"{hashes} {project.title}\n\n"
        f"**Project ID:** `{project.id}`\n\n"
        f"**One-liner**\n\n{md_escape(project.one_liner)}\n\n"
        f"**Context**\n\n{md_escape(project.context)}\n"
    )


def render_subgroup(subgroup: Subgroup) -> str:
    parts = [
        f"## {subgroup.title}",
        "",
        "**One-liner**",
        "",
        md_escape(subgroup.one_liner),
        "",
        "**Context**",
        "",
        md_escape(subgroup.context),
        "",
    ]
    if subgroup.projects:
        parts.extend(["### Projects", ""])
        for project in subgroup.projects:
            parts.append(render_project(project, heading_level=3))
    return "\n".join(parts).rstrip() + "\n"


def render_group_page(group: TopGroup, position: int) -> str:
    parts = [
        "---",
        f'title: "{group.title.replace(chr(34), chr(34) * 2)}"',
        f"sidebar_position: {position}",
        f'description: "{group.one_liner.replace(chr(34), chr(34) * 2)}"',
        "---",
        "",
        f"# {group.title}",
        "",
        f"**Group ID:** `{group.id}`",
        "",
        "## One-liner",
        "",
        md_escape(group.one_liner),
        "",
        "## Context",
        "",
        md_escape(group.context),
        "",
    ]

    if group.projects:
        parts.extend(["## Projects", ""])
        for project in group.projects:
            parts.append(render_project(project, heading_level=2))

    if group.subgroups:
        parts.extend(["## Subgroups", ""])
        for subgroup in group.subgroups.values():
            parts.append(render_subgroup(subgroup))

    return "\n".join(parts).rstrip() + "\n"


def render_index(groups: OrderedDict[str, TopGroup], base_path: str) -> str:
    parts = [
        "---",
        'title: "Control Tower Context"',
        "sidebar_position: 1",
        'description: "Contexto navegable de grupos y proyectos del portfolio."',
        "---",
        "",
        "# Control Tower Context",
        "",
        "Esta documentación fue generada automáticamente a partir de un CSV estático con grupos y proyectos del portfolio.",
        "",
        "## Groups",
        "",
    ]

    for group in groups.values():
        subgroup_count = len(group.subgroups)
        project_count = len(group.projects) + sum(len(s.projects) for s in group.subgroups.values())
        slug = slugify(group.title)
        parts.append(
            f"- [{group.title}](./{slug}/index.md)  ")
        parts.append(
            f"  {group.one_liner}  ")
        parts.append(
            f"  Group ID: `{group.id}` | Projects: {project_count} | Subgroups: {subgroup_count}")
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_docs(csv_path: Path, docs_root: Path, section_dir: str = "control-tower") -> None:
    rows = load_rows(csv_path)
    groups = build_tree(rows)

    out_root = docs_root / section_dir
    out_root.mkdir(parents=True, exist_ok=True)

    write_text(
        out_root / "_category_.json",
        json.dumps(
            {
                "label": "Control Tower",
                "position": 1,
                "link": {"type": "doc", "id": f"{section_dir}/index"},
            },
            ensure_ascii=False,
            indent=2,
        ) + "\n",
    )

    write_text(out_root / "index.md", render_index(groups, section_dir))

    for position, group in enumerate(groups.values(), start=1):
        group_slug = slugify(group.title)
        group_dir = out_root / group_slug
        write_text(
            group_dir / "_category_.json",
            json.dumps(
                {
                    "label": group.title,
                    "position": position,
                    "link": {"type": "doc", "id": f"{section_dir}/{group_slug}/index"},
                },
                ensure_ascii=False,
                indent=2,
            ) + "\n",
        )
        write_text(group_dir / "index.md", render_group_page(group, position))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build Docusaurus markdown docs from a Control Tower context CSV."
    )
    parser.add_argument(
        "--csv",
        default="portfolio_context.csv",
        help="Path to the source CSV.",
    )
    parser.add_argument(
        "--docs-root",
        default="docs",
        help="Path to the Docusaurus docs root.",
    )
    parser.add_argument(
        "--section-dir",
        default="control-tower",
        help="Subdirectory inside docs/ where files will be generated.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    build_docs(Path(args.csv), Path(args.docs_root), args.section_dir)
