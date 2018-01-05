# Why do version control?
https://phdcomics.com/comics/archive.php?comicid=1531

Think of version control like tracked changes in a word document in a shared folder, just amultiplied across serveral revisions of that document and well, better. 
Every time you commit changes it creates a log of what it was before, after and your commit comments describing what you did or why. If tomorrow you realize your code doesn't work anymore you can easily restore all or part of a previous version until it works again.

Here are my top reasons for using version control:
1. Store versions properly (saves every commit)
2. Transparent (everyone can see every change you ever made)
3. Collaboration (I easily update what is on my home machine based on commits I made at work today)

# GitHub
There is an official [USEPA GitHub account](https://github.com/USEPA)
Before putting anything there review their [guidelines](https://usepa.sharepoint.com/sites/AO_FOIA_Centralization/Shared%20Documents/Office%20of%20Public%20Affairs/Collected%20OPA%20Documents/EPA-HQ-2017-004882/GitHub%20Guidance%20_%20Web%20Guide%20_%20US%20EPA.pdf)

My short version would be: 
1. Don't put anything up in a public repository that isn't already reviewed and public.
2. Even private repositories shouldn't contain protected or propriatary code.
3. Remember it saves every version so deleting something later isn't an option (e.g. passwords, keys, etc.).
4. Use it for code not documents.

# Integration with IDE:
Instructions for setting up GitHub repositories in RStudio:
https://support.rstudio.com/hc/en-us/articles/200532077?version=1.1.383&mode=desktop

Instructions for setting up GitHub Projects in spyder:
https://pythonhosted.org/spyder/projects.html
