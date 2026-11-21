# Introduction to Programming



## Programming introduction



1. **What is Programming?**



* At its core, programming is creating a sequence of instructions to enable a computer to do something specific (such as calculations, displaying info, or saving files).
* This set of instructions is known as a program or software.



2\. The Two Main Components of Programs



* Data: The information that the program processes.
* Algorithms: The instructions that operate on that data.



3\. A Quick Look at Python Code



* Programs take data, process it, and output/store the result.
* Concepts introduced include variables (acting like boxes to store data like numbers) and functions like print (built-in instructions that do specific tasks, such as showing results on the screen).



4\. Why Do We Program?



* Computers are extremely fast (processing millions of instructions per second) and reliable (following instructions precisely).
* However, computers cannot think or make decisions on their own; they strictly follow what the programmer tells them to do.
* Therefore, programming involves developing two key skills: problem-solving and writing code.



## Python overview



1. What Python is: A high-level, multi-paradigm programming language designed to be easy for humans to read and understand, with a simple and expressive syntax.



2\. What we can use Python for: Desktop applications, web servers, automation scripts (like backup tools), data analysis, and artificial intelligence.



3\. Advantages for beginners: It has a rich set of learning materials, it is open source (free to use and inspect), and its syntax resembles English, making it very friendly as a first programming language.



## Console/terminal



1. What the Terminal Is: A text-based interface used to interact with your operating system, where you type commands instead of clicking buttons and menus. We also look at the terms Terminal (the window), Shell (the program that reads your commands), and Console (often used informally as a synonym).



2\. GUI vs. Terminal: Both serve the same goal—telling the computer what to do—but use different interfaces (visual elements and a mouse versus typed text).



3\. Why Developers Use It: It offers speed, precision, automation, and seamless integration with developer tools like Git, package managers, and servers.



4\. Basic Commands: A few beginner commands help you navigate:



* pwd: Shows where you are currently located.
* ls: Lists files and folders.
* cd: Moves you to another folder.



## Development Environment



1. What is development environment?



* It is not just a single tool or program; it is your complete coding workspace and a combination of multiple tools that work together to help you build software.



2.Why It Matters for Beginners



* Learning how the environment works reduces confusion. Instead of feeling overwhelmed by separate windows, editors, and terminals, you learn to see them as a connected system following a basic cycle: Write → Run → Check → Fix.



3\. The Key Components of a Development Environment



* Code Editor / IDE: Where you write and edit your code (e.g., VS Code, PyCharm).
* Programming Language \& Interpreter/Runtime: The instructions you write and the engine that executes them (e.g., Python code executed by the Python interpreter).
* Terminal: A text-based interface used to interact with the system, run programs, and navigate project folders.
* Project Files and Folders: How your code is organized (e.g., main.py).
* Output / Result Viewer: Where you see the outcome of your program (which for beginners is often the terminal or console).



## Variables



1. What is a Variable?



* Software combines data and algorithms. Variables are used to store and manage data so we can use it in our programs.
* A variable is a combination of a value and a name (e.g., assigning the value 42 to the name X, or the text/string "Thomas" to the name Cat).



2\. Using Variables in Operations



* When we use a variable, we are actually using the value stored inside it, not the variable name itself.
* Evaluation order: In an assignment statement, the right-hand side is always evaluated before the left-hand side. For example, in C = A + B, Python first looks up the values inside A and B, adds them together, and then stores the new result into C.



3\. Overwriting Values



* A variable can hold only a single value at a time. If you assign a new value to an existing variable name, the old value is overwritten and forgotten.



4\. The Importance of Definition Order



* Variables must exist before they are used.
* Because Python executes code from top to bottom, trying to use a variable before it has been defined will result in a NameError.



5\. Naming Conventions



* Variable names should be descriptive and meaningful to humans (avoiding random strings like ASADFG).

When a variable name consists of multiple words, we use naming conventions to make them readable since spaces aren't allowed:

&#x09;- snake\_case (words separated by underscores, which is the convention preferred in this course

&#x09;- camelCase (subsequent words start with a capital letter)

* It is best to choose one convention and stick to it consistently.



## Code structure



1. Indentation:



* What indentation is (the empty spaces at the beginning of a line).
* Why spacing has syntactic meaning in Python (unlike in many other programming languages).
* How statements within the same block must share the exact same indentation level, or else Python will throw an IndentationError and refuse to run the code.



2\. Comments:



* What comments are (arbitrary text that is completely ignored by the Python interpreter).
* How they are written (starting with a hash symbol #, and usually highlighted in green in editors like Visual Studio Code).
* What they are used for (adding explanations about what the code does, or temporarily disabling/commenting out lines of code during testing).

