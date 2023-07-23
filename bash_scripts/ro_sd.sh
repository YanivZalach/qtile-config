#!/usr/bin/env bash

# Get hidden bags
set -euo pipefail

# Main function
main() {
    # Show a rofi menu with two options: "shutdown" and "reboot"
    choice=$(printf '%s\n' "shutdown" "reboot"  | rofi -dmenu -lines 3 -p "Y4Z - Do")

    case "$choice" in
        "shutdown")
            # Ask for confirmation before shutting down
            confirm_action "Shutdown" "Are you sure you want to shut down?"
            # Perform the system shutdown
            shutdown -h now
            ;;
        "reboot")
            # Ask for confirmation before rebooting
            confirm_action "Reboot" "Are you sure you want to reboot?"
            # Perform the system reboot
            reboot 
            ;;
        *)
            # Invalid choice, display an error message and exit with a non-zero status
            echo "Invalid choice: $choice"
            exit 1
            ;;
    esac
}

# Function to confirm the chosen action
confirm_action() {
    local action_name=$1
    local message=$2

    # Show a rofi prompt with "yes" and "no" options for confirmation
    local confirm_result=$(echo -e "yes\nno" | rofi -dmenu -p "$action_name - $message" -lines 2)
    
    if [ "$confirm_result" == "yes" ]; then
        # User confirmed the action, return success (exit status 0)
        return 0
    else
        # User declined the action, exit the script with a success status (exit status 0)
        exit 0
    fi
}

# Call the main function to start the script
main
