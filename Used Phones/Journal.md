# 2020-09-13

    - Issues with parsing listings where certain attributes were missing. 
    - Could parse for individual elements by name but seems very verbose and cumbersome
        - If going down this path maybe better to create dictionary?
            - keys are name of attribute (eg. list date, price, colors)
        - Then use pandas from_dict

# 2020-09-14

    - Look up mapping for dictonary, going to write a simple for loop for now better readability
    - Build plan for more automated navigation, stopgap is to general list of urls to loop through
    - Clean up description (non alphanumeric characters)
    - Some of the categories are mislabeled
    - Next is to add a couple more websites then do some NLP research