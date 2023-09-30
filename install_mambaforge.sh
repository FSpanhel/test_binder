# Download the most current mambaforge version and install
mamba_folder="~/mambaforge"  # Location where mambaforge is installed.

# Download
url="https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
mamba="Mambaforge-$(uname)-$(uname -m).sh"
echo -e "\n> Download $url into ~ and install in batch mode (license terms are automatically accepted and the installation destination is $mamba_folder)."
wget -P ~ $url
bash ~/$mamba -b -p $mamba_folder

# Initialize shells:
echo -e "\n> Initialize activation scripts for bash and zsh."
dry_run "source $mamba_folder/bin/activate"
dry_run "mamba init bash || true"
dry_run "mamba init zsh || true"

# Remove mambaforge download
echo -e"\n> Remove downloaded mamba installation file $mamba."
rm ~/$mamba

# Source rc files so that commands are known and we don't have to open a new session
echo -e "\n> Source ~/.bashrc and ~/.zshrc so that we don't have to start a new session."
dry_run "source ~/.bashrc || true"
dry_run "source ~/.zshrc || true"
