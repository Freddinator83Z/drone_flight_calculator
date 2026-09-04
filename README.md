# Drone Flight Calculator

This project calculates a drone's active flight time based on payload weight. It also generates a table of flight times for a range of payload weights.

## AI-Use Disclosure

Used GitHub Copilot inline suggestions while implementing the flight-time calculator and GitHub Copilot Chat (/tests) to help generate the initial pytest tests.

I reviewed and made note of Copilot's suggestions, rejected an incorrect suggestion that used the wrong flight-time formula, edited a suggestion so flight time could not go below zero, and accepted correct suggestions where appropriate.

I also reviewed the generated tests and corrected their indentation so pytest discovered all four required cases. I verified that the tests covered zero payload, a typical payload, the zero-flight-time boundary, and a negative weight input.

I also verified all tests pass using pytest.