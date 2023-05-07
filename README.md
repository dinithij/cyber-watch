# cyber-watch

Cyber Watch Python Library User Manual

Cyber Watch Python Library is a tool that helps in identifying cyberbullying content in a given text. It provides users with an easy-to-use library that can be installed using pip install command. 


# Installation

`pip install cyberwatch`

Once installed, it can be imported to the code using the following command:

`from cyberwatch.cyber_watch import CyberWatch`

# Usage

The CyberWatch class can then be used to create an object that will be used to predict whether a given text contains cyberbullying content or not.

## Creating an object
To create an object from the CyberWatch class, use the following command:

`cyb_watch = CyberWatch()`

## Predict function
After creating an object, the predict function can be called to predict whether a given text contains cyberbullying content or not.

The syntax for the predict function is as follows:

`pred = cyb_watch.predict("Input String to Validate")`

The predict function takes a string input and returns a string value "cyberbullying" or "not_cyberbullying".

## Disabling Data Preprocessing Features
Users also have the option to disable some features from data preprocessing level such as spelling mistake fix, Hashtage map, and abbreviation/Slang map. By default, all three options are enabled.

To disable a feature, a parameter needs to be passed to the predict function. The parameter names are as follows:

### To disable spelling correction -> {"spelling": False}
### To disable Hashtag split -> {"hashtag": False}
### To disable abbreviation/Slang map -> {"slang": False}

An object can be created to contain the value of the parameter as follows:

`spel_param = {"spelling": False}`

The parameter can then be passed to the predict function using the following command:

`pred = cyb_watch.predict("Input String to Validate", **spel_param)`

# Conclusion
Cyber Watch Python Library is a useful tool that can help users to identify cyberbullying content in a given text. By following the instructions in this manual, users can easily install and use the library to predict whether a given text contains cyberbullying content or not.
