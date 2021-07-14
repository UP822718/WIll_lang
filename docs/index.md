# WILL-LANG

## index
1. pros and cons
1. Security
    1. Actor model
    1. Capability-based security
    1. Access modifiers
1. coming soon Testing by model checking
    1. inline
    1. Linear bounded automaton
1. coming soon Testing by unit testing and symbolic unit testing
1. coming soon Error recvery
1. coming soon Dymaic software updates
1. coming soon suspend and suspend to disk

## pros and cons

### pros
1. we have some recursion
2. all programs created in the strictly programming language are going to to halt
3. tools with the programming language guaranteed that programs can be bug-lass because of exhaust search 
4. the programming language has two different security models not commonly found in other programming languages
### cons
1. the language isn't Turing complete
2. can only primitive recursion
## Security
### Actor model
### Capability-based security
### Access modifiers
## type of objects
## data types
### f
### f
### f
## unit testing and symbolic unit testing

## Testing by model checking
by using ``___`` command to run your codes you be able to test if your program has any bugs. 
## inline
the inline model makes a programmer have to tell the computer what the expected values would be at any different time .this is done this is done by the programming determining if the program can hit any asserts are true or if any assume to be false when the prgamine is running. assume can additionally speed-up the program such as it can help limit the search space for each individual possible variable as it has to try values.
| function name      | parameter           | Description |
| -----------        |---------------------| ----------- |
| asserts            | bool                | Title       |
| named_asserts      | string , bool       | Title       |
| assertEquals       | string , any,any    | Text        |
| assume             | bool                | Text        |
| named_assume       | string , bool       | Text        |
| named_cover        | string , bool       | Text        |
| cover              | bool                | Text        |
| label              | string              | Text        |
| error              | string              | Text        |
| trace_print        | string              | Text        | 

## finite state lang
additionally another way of using model checking that can be used in conjunction with the previous that was a fine each other possible States the program should be able to get into along with expected outputs. this allows for the small deeper analysis of the program to compare if it complies with the financial state machine then the inline model.

| function name      | parameter           | Description |
| -----------        |---------------------| ----------- |
| before_call        | none or ref         | will stop execution of software under test at before the next
| after_call         | none or ref         | will stop execution of software under test at 
| before_call        | none or ref         | will stop execution of software under test at before the next
| after_call         | none or ref         | will stop execution of software under test at 
| after_label        | none or ref         | will stop execution of software under test at before the next
| before_label       | none or ref         | will stop execution of software under test at 
| after_read         | none or ref         | will stop execution of software under test at before the next
| before_write       | none or ref         | will stop execution of software under test at 
| after_retun        | none or ref         | will stop execution of software under test at after the next returns if none caller function is specified or it wait for a retrun for that function|
| before_retun       | none or ref         | will stop execution of software under test at 
| after_after_for    |                     |
| before_before_for  |                     |
| after_after_while  |                     |
| before_before_while|                     |
| before_return      | ref                 |
| after_return       | ref                 |
| after_line         | int                 |
| before_line        | int                 |
| resume             | none                |
## operation
## simple data types
## complexed
