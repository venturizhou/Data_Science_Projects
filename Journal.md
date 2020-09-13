2020-09-13
    - Issues with parsing listings where certain attributes were missing. 
    - Could parse for individual elements by name but seems very verbose and cumbersome
        - If going down this path maybe better to create dictionary?
            - keys are name of attribute (eg. list date, price, colors)
        - Then use pandas from_dict