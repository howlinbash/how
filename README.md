# How

A _very_ simple command line interface for my [manual](https://github.com/howlinbash/manual)

## Usage

Manual pages are referenced by 'tags'. 

```bash
how <tag>
```

The default behaviour opens a manual page in Vim.

```bash
how git
```

You can also open a page in the browser.

```bash
how -v git
```

Print the manual contents with:

```bash
how -c
```

List all the tags with:

```bash
how -l
```
