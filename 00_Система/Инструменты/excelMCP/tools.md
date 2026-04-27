# Excel MCP Server Tools

This document provides detailed information about all available tools on the Excel MCP server. Currently, this is not a classic MCP.
The algorithm of operation is described below.
The program is written in Pascal, so paths are written in the format C:\path\... (with backslashes).

## Principle of Operation

Before starting, you should carefully study all functions to devise an optimal algorithm for working with Excel files.
The program operates in server mode, awaiting commands. Interaction occurs through files in the `excel-mcp` directory:

1.  **Sending a command**: To issue a command, the client (e.g., Gemini) creates a `command.in` file in the `excel-mcp` folder. The file must contain a single line with the command (e.g., `create_workbook`).
2.  **Executing the command**: The server constantly monitors for the appearance of the `command.in` file. As soon as the file is detected, the server reads the command from it, executes it, and then deletes `command.in`.
3.  **Receiving the result**: After executing the command, the server writes the result (success message or error description) to the `command.out` file in the same directory.
4.  **Client verification**: The client can read the `command.out` file to find out the result of its command execution.
5.  **Starting work**:
    5.1 When starting work, the LLM should first check if ExcelMcpPrj.exe is running. You can check the launch by checking for the process in the system or by the log file `Log.txt`.

    **5.1.1 IMPORTANT: Problem with LLM Gemini startup**
    Direct server startup from the Gemini environment (`run_shell_command`) leads to unstable operation. The process starts, but Gemini cannot properly track its state, which leads to model "hanging" and subsequent crash of the server when the operation is cancelled.

    **Reliable solution — startup via `.bat` file:**
    - Create a `start_server.bat` file in the `excel-mcp` folder with the following content:
      ```bat
      @echo off
      cd /d "%~dp0%"
      START "MCP Server" ExcelMcpPrj.exe
      ```
    - Running this `.bat` file creates a completely independent server process in a separate console window. Gemini can launch this file and, without hanging, continue working, interacting with the already running server.

    5.2 If the server is not running, it should be launched using `start_server.bat`
    5.3 Next, the LLM adds commands to the `command.in` file and checks their execution by reading `command.out`. The server deletes `command.in` after processing, so the LLM understands that the command has been processed.
    5.4 The server may process commands with a delay. Instead of a fixed wait, the following algorithm is recommended:
    a. After sending a command to `command.in`, start checking for the existence of `command.out` at a short interval (e.g., 1 second).
    b. If the `command.out` file does not appear, continue checking, increasing the total waiting time up to 15 seconds.
    c. If the file has not appeared after 15 seconds, it should be assumed that the server is not responding, and a decision should be made on further actions (e.g., notify the user or try to restart the server).
    5.5 When opening or creating a workbook, you should clarify sheet names, as sheets may be called differently in different regions, or the user may rename them. If you create a new workbook, you can refer to the sheet not by name but by index
    5.6 When reading information in a workbook, you should use the `get_sheet_dimensions` command to know which cells to read with the `read_range` command
6. If within 15 seconds the LLM does not receive a response in command.out, it should stop trying;
7. **Ending work**: The `quit_excel` command only closes the Excel application, but **does not stop the server** (`ExcelMcpPrj.exe`). To completely stop the server, you must terminate its process. You can use the `stop_server` command for this.

This file-based mechanism provides simple asynchronous interaction with the running server.

**Processing multiple commands**
It is acceptable to write several commands at once in the command.in file, for each command a separate line will be formed in the command.out file
Example:
 set_cell --sheet_name "Sheet 1" --cell "B3" --value "str1"
 set_cell --sheet_name "Sheet 1" --cell "B4" --value "str2"
 set_cell --sheet_name "Sheet 1" --cell "B5" --value "str3" 

### Executing Commands via HTTP

In addition to file exchange, the `ExcelMcpPrj.exe` server allows executing commands directly via HTTP GET requests. The server accepts requests on port `8080`. This is the preferred method for integrations.

**Request Format:**
`http://localhost:8080/?command=COMMAND`

Where `COMMAND` is the full command string, identical to the one used in the `command.in` file.

**Important:** All special characters in the command (spaces, quotes, backslashes, etc.) must be properly URL-encoded.

**Examples:**

*   **Check server status (without the `command` parameter):**
    `http://localhost:8080/`
    *Response: `server is running...`*

*   **Open a workbook (with URL encoding):**
    *   Command: `open_workbook --filepath "C:\My Docs\report.xlsx"`
    *   Request: `http://localhost:8080/?command=open_workbook%20--filepath%20%22C%3A%5CMy%20Docs%5Creport.xlsx%22`

*   **Set a cell value:**
    *   Command: `set_cell --sheet_name "Sheet1" --cell "A1" --value "Test Value"`
    *   Request: `http://localhost:8080/?command=set_cell%20--sheet_name%20%22Sheet1%22%20--cell%20%22A1%22%20--value%20%22Test%20Value%22`

**Server Response:**
*   On successful command execution, the server will return a text response with the result of the execution.
*   Example response for `get_sheet_dimensions`: `Rows: 10, Cols: 5`

## Excel Operations

### run_excel

Launches the Excel application. **Note:** Usually not required, as launching `ExcelMcpPrj.exe` automatically opens Excel.

`run_excel`
Example: `run_excel`

**Possible errors:**
- `Excel already started`: If Excel is already running.

### quit_excel

Closes the Excel application. **Important:** This command does not stop the `ExcelMcpPrj.exe` server.

`quit_excel`
Example: `quit_excel`

### stop_server

Stops the server, terminating the `ExcelMcpPrj.exe` process and closing Excel.

`stop_server`
Example: `stop_server`

### ping_server

Checks if the server is running and responding.

`ping_server`
Example: `ping_server`

- Returns: `pong` if the server is active.

## Workbook Operations

### create_workbook

Creates a new Excel workbook.

`create_workbook`
Example: `create_workbook`

**Possible errors:**
- `Error: Failed to create workbook`: If failed to create workbook.

### open_workbook

Opens an existing Excel workbook.

`open_workbook --filepath <path>`

- `filepath`: Path to the Excel file
Example: `open_workbook --filepath "C:\Users\User\Documents\test.xlsx"`

**Possible errors:**
- `Error: Failed to open workbook: <filepath>`: If failed to open workbook at the specified path.

### save_workbook

Saves the active Excel workbook.

`save_workbook --filepath <path>`

- `filepath`: Path for saving
Example: `save_workbook --filepath "C:\Users\User\Documents\test_saved.xlsx"`

**Possible errors:**
- `Error: Failed save WorkBook, no active workbook`: If there is no active workbook to save.
- `Error: Failed save, path not exists - <filepath>`: If the specified save path does not exist.

### close_workbook

Closes the active Excel workbook.

`close_workbook`
Example: `close_workbook`

**Possible errors:**
- `Error: Failed to close workbook`: If failed to close workbook.

## Sheet Operations

### get_sheet_names

Gets a list of all sheet names in the active Excel workbook.

`get_sheet_names`
Example: `get_sheet_names`

- Returns: A string with sheet names separated by commas (e.g., "Sheet1,Sheet2,Sheet3").

**Possible errors:**
- `Error: Failed to get sheet names`: If failed to get sheet names.

### get_sheet_dimensions

Gets the dimensions of the used range on the sheet (using the reliable `SpecialCells(xlCellTypeLastCell)` method).

`get_sheet_dimensions --sheet_name <name>`

- `sheet_name`: Sheet name
Example: `get_sheet_dimensions --sheet_name "Sheet1"`
- Returns: Number of rows and columns in the format "Rows: X, Cols: Y"

## Cell Operations

### set_cell

Writes a value to a cell. It is not allowed to try to write many cells with this command without checking the result in command.out or Http (depending on the method of operation).

`set_cell --sheet_name <name> --cell <cell> --value <value>`

- `sheet_name`: Sheet name
- `cell`: Cell address (e.g., A1)
- `value`: Value to write
Example: `set_cell --sheet_name "Sheet1" --cell "A1" --value "Hello"`

**Possible errors:**
- `Error: Failed to set cell, Workbook not opened`: If workbook is not opened.
- `Error: Failed to set sheet <sheet_name>`: If the specified sheet does not exist.
- `Error: Failed to set cell <cell>`: If the specified cell address is invalid.

### get_cell

Reads a value from a single cell.

`get_cell --sheet_name <name> --cell <cell>`

- `sheet_name`: Sheet name
- `cell`: Cell address (e.g., A1)
Example: `get_cell --sheet_name "Sheet1" --cell "A1"`
- Returns: Cell value

**Possible errors:**
- `Error: Failed to get cell, Workbook not opened`: If workbook is not opened.
- `Error: Failed to get cell, sheet not exists <sheet_name>`: If the specified sheet does not exist.
- `Error: Failed to get cell <cell>`: If the specified cell address is invalid.

### read_range

Reads a range of cells as text. #13#10 - newline; #9 - tab
Cell addresses should be determined taking into account special characters.

`read_range --sheet_name <name> --start_cell <cell> --end_cell <cell>`

- `sheet_name`: Sheet name
- `start_cell`: Start cell of the range (e.g., A1)
- `end_cell`: End cell of the range (e.g., D4)
Example: `read_range --sheet_name "Sheet1" --start_cell "A1" --end_cell "B5"`
- Returns: Text where columns are separated by tabs (`	`) and rows by newlines (`
`). Empty cells are represented by empty strings between delimiters.

**Possible errors:**
- `Error: Failed to set cell, Workbook not opened`: If workbook is not opened.
- `Error: Failed to read range, sheet not exists <sheet_name>`: If the specified sheet does not exist.
- `Error: Failed to read range <start_cell>:<end_cell>`: If the specified range is invalid.

### get_cell_color

Reads the background color of a cell.

`get_cell_color --sheet_name <name> --cell <cell>`

- `sheet_name`: Sheet name
- `cell`: Cell address (e.g., A1)
Example: `get_cell_color --sheet_name "Sheet1" --cell "A1"`
- Returns: Numeric color value (integer).

**Possible errors:**
- `Error: Failed to get cell color, Workbook not opened`: If workbook is not opened.
- `Error: Failed to get cell color, sheet not exists <sheet_name>`: If the specified sheet does not exist.
- `Error: Failed to get cell color, invalid cell <cell>`: If the specified cell address is invalid.

### set_cell_color

Sets the background color of a cell.

`set_cell_color --sheet_name <name> --cell <cell> --color <color>`

- `sheet_name`: Sheet name
- `cell`: Cell address (e.g., A1)
- `color`: Numeric color value (integer). For example, 255 for red, 65280 for green.
Example: `set_cell_color --sheet_name "Sheet1" --cell "A1" --color 255`

**Possible errors:**
- `Error: Failed to set cell color, Workbook not opened`: If workbook is not opened.
- `Error: Failed to set cell color, sheet not exists <sheet_name>`: If the specified sheet does not exist.
- `Error: Failed to set cell color, invalid cell <cell>`: If the specified cell address is invalid.

## Information Search

### find_in_workbook

Searches for the specified text across all worksheets in the active Excel workbook.

`find_in_workbook --text <text_to_search>`

- `text`: Text or part of the text to search for.
Example: `find_in_workbook --text "some text"`
- Returns: A string containing a list of found matches. Each match is presented in the format "SheetName,CellAddress,CellValue" and separated by a newline (`
`). If no matches are found, an empty string is returned.

**Possible errors:**
- `Error finding in workbook: <error_message>`: If an error occurred during the search.