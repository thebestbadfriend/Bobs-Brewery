# Summary
This module creates a "contacts" tab which includes a treeview in which contacts can be viewed as well as options to search, add, update, and delete contacts
- - -
# Technical Notes
The interface here is intended to be something along these lines in order to not tightly bind the module to a single data model or hierarchy

### Configuration
The data source, tree hierarchy, and arguments passed to the populator function (such as database_name and query) for each level of the hierarchy can be configured in the contacts_treeview.json file. For example:

```
```