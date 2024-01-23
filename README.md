# Test to act on GitHub Actions Issue

This is a test for a GitHub action to add on a new or edited GitHub issue.

## Usage

1. Create a new issue or edit one that you've already opened
2. Watch the action go and print out every other line of the issue

## Parser

The parser is a simple python package called `ghactmod`.
The issue body is passed to `ghactmod.run` as a multiline string.
The parser then just takes all odd-numbered lines and prints them out.

## What this can be used for

The idea behind this test is that
such a workflow can be used for modifying a static website.
The idea would be to have a website with a database that is based in text files,
which are stored in the repo.
An issue template to add a new entry to the database would be created.

The action then would parse the issue body and create a new file for the database.
A PR is automatically opened for the maintainer to review the change.
If okay and the PR is merged, 
a second action will the extended database plus the static pages
and deploy a new `github-pages` site.
