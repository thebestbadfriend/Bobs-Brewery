# Summary
This module creates a "contacts" tab which includes a treeview in which contacts can be viewed as well as options to search, add, update, and delete contacts
- - -
# Technical Notes
The interface here is intended to be something along these lines in order to not tightly bind the module to a single data model or hierarchy

### Configuration
The data source, tree hierarchy, and arguments passed to the populator function (such as database_name and query) for each level of the hierarchy can be configured in the contacts_treeview.json file. For example:

```
```
- - -
# Other Notes
- I really think this can be set up such that there does not need to be a specific populator for each treeview but where a generic treeview populator can be directed by the json how to behave
  - This would abstract treeview population in such a way that non tech people can still add treeviews - if only they can represent the data hierarchy - without having to understand how to populate them.
  - I will probably, when all is said and done, put that functionality into a "pop_treeview_level_from_query" function or similar
- Also, the names of things in the json do not have to match the code. "pack_properties" for example, is not likely to make sense to the average user, but "display_settings" would and can be converted in code to "pack_properties" when needed. Similarly, `"fill": "BOTH"` is less likely to make sense than `"expand horizontally": "true", "expand vertically": "true"`, which can also be converted by the code when needed