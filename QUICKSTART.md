# Git this Thing Going!

`git clone https://github.com/mitchell-reynolds/hw-for-branch.git`

# Set Up The Required Packages in the correct environment
Personally, I use [Anaconda3](https://www.anaconda.com/download/?lang=en-us#macos) on my iMac. 
Python 3.6 is needed for some of the requirements later on.    
`conda create -n ml python=3.6`  
`source activate ml`    
`pip install -r mitchell-requirements.txt`

# Download the Data
Simply place the downloaded data under the `data`. Note, I've added a `.gitignore` so that the Branch.co data
stays private.

Since this is a one-off project and the file is private on Google Drive, the process of scripting is doable but unnecessary.
If we needed to repeatably download new data, then we'd build a database instead.

# Run some code to get up and running
These 3 scripts will unzip the files (once they're in the data directory) into the data directory. 
Then, we'll check if we're able to build the dataframes before any fun modeling. 
Then, _we model_. 
```
python properly_unzip_files.py  
python build_dataframes.py
python run_baseline_model.py
```

Note if the formatting is strange to you, I use a friend's autoformatter called Black. 
Might take some getting used to for those first-time seeing it. 
