# 341-DFA
DFA-based validator for email-like strings using custom state transitions and trap state handling.

## Email Validator (DFA)
Implements a deterministic finite automaton (DFA) in Python to validate strings that resemble email addresses. The DFA processes input character-by-character, following strict transition rules and utilizing trap states to reject malformed strings. Includes automated output logging to output263.txt.

## Tech: 
Python, FSM Design

## Features:
Alphabetic and symbol parsing (@, .)
Trap state logic for invalid transitions
Logs results to file with test case tracking
