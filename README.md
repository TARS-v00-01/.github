# TARS-v00-01 community

This public repository hosts the organization's profile, membership request form, and approval automation.
It does not contain private application or firmware source.

[Request organization membership](https://github.com/TARS-v00-01/.github/issues/new?template=membership-request.yml)

An organization owner approves a request by commenting `/approve-membership`. The bot then sends a regular-member
invitation to the request author. After accepting it, the person receives the organization's existing Read access
to all private repositories, including documentation. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full process.

The [public profile](profile/README.md) appears on the [organization overview](https://github.com/TARS-v00-01).
Contributors use private forks and pull requests for proposed fixes. Maintainers take accepted changes through
Gerrit review, CI, and submission before GitHub publication.

## Verification and publication

The Gerrit project is `.github`. Upload changes to Gerrit `refs/for/master`; never push source directly to the
GitHub upstream. Only the exact submitted `master` revision is replicated. This repository has its own module CI
and is not pinned or uplifted as a hardware or application component.

```bash
python3 -m unittest discover -s .github/scripts/tests -v
python3 ci/validate.py
```

GitHub runs the same tests on submitted changes. The **Organization membership requests** workflow's **Run workflow**
action checks the configured invitation credential without inviting anybody. Store the dedicated token as an
Actions secret available only to this repository; see [credential setup](CONTRIBUTING.md#automation-configuration).
