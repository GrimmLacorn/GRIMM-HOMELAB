#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
gitleaks_image="ghcr.io/gitleaks/gitleaks@sha256:c00b6bd0aeb3071cbcb79009cb16a60dd9e0a7c60e2be9ab65d25e6bc8abbb7f"

if ! docker image inspect "$gitleaks_image" >/dev/null 2>&1; then
  docker pull "$gitleaks_image"
fi

docker run --rm --read-only --network none \
  --volume "$repo_root:/repo:ro" \
  "$gitleaks_image" git --redact --no-banner /repo
