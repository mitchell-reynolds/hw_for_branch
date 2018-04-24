# Git this Thing Going!

`git clone https://github.com/mitchell-reynolds/hw-for-branch.git`

# Set Up The Required Packages
This is currently a work-in-progress since I'm working on the analysis.
`pip install -r mitchell-requirements.txt`

# Download the Data
Simply place the downloaded data under the `data`. Note, I've added a `.gitignore` so that the Branch.co data
stays private.

Since this is a one-off project and the file is private on Google Drive, the process of scripting is doable but unnecessary.
If we needed to repeatably download new data, then we'd build a database instead.

# Run some code to get up and running

`python properly_unzip_files.py`
`python build_dataframes.py`

Note if the formatting is strange to you, I use a friend's autoformatter called Black. 
Might take some getting used to for those first-time seeing it. 
