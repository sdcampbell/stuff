# login-loop
Metasploit resource script for looping time-delayed login attacks, such as owa_login.

# Details
This is a Ruby resource script for Metasploit. The usage scenario is that you want to take a module like `owa_login`, and run it with a different password at a set interval. The script will read a list of the passwords you want to run, and at the set interval, write each one to a pass file and run the current module.

For example:
  1. Create the list of passwords you want to run through as `pass_input.txt`.
  2. Start Metasploit and load your module, such as `owa_login`.
  3. Configure your other parameters, such as `RHOST`/`RHOSTS` and `USER_FILE`.
  4. Set the `PASS_FILE` to `pass_file.txt`.
  5. From the Metasploit prompt, run `resource login-loop.rc`.
  6. The script will read each line of `pass_input.txt`, and:
     1. Run the `date` command to leave you with a handy timestamp.
     2. `echo` the current `pass_input.txt` line to `pass_file.txt`.
     3. `run` the Metasploit module.
     4. Start all subsequent executions of the loop with a `sleep` command, set to 1,860 seconds (31 minutes) by default.
