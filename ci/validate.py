#!/usr/bin/env python3
"""Validate organization profile and fixed membership workflow configuration."""
import ast
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
for path in (root / ".github/scripts").rglob("*.py"):
    ast.parse(path.read_text(), filename=str(path))
config = json.loads((root / ".github/contributor-access.json").read_text())
assert config["organization"] == "TARS-v00-01"
assert config["request_repository"] == ".github"
assert config["approval_command"] == "/approve-membership"
assert config["invitation_role"] == "direct_member"
assert config["default_repository_permission"] == "read"
assert "blank_issues_enabled: true" in (root / ".github/ISSUE_TEMPLATE/config.yml").read_text()
profile = (root / "profile/README.md").read_text()
request = "https://github.com/TARS-v00-01/.github/issues/new?template=membership-request.yml"
assert request in profile
assert request in (root / "CONTRIBUTING.md").read_text()
workflow = (root / ".github/workflows/membership-requests.yml").read_text()
assert "github.repository == 'TARS-v00-01/.github'" in workflow
assert "github.ref == 'refs/heads/master'" in workflow
assert "ref: ${{ github.sha }}" in workflow
assert workflow.count("runs-on: ubuntu-24.04") == 3
assert "runs-on: self-hosted" not in workflow
assert "pull_request_target:" not in workflow
assert "persist-credentials: true" not in workflow
assert "ci/validate.py" in workflow
print("Organization profile, membership configuration, and hosted workflow validation passed.")
