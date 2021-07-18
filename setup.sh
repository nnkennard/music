if [[ "$(python3 -V)" =~ "Python 3" ]];
then
	echo "Python 3 is installed"
else
	echo "Please ensure that Python 3 is installed."
exit
fi

python3 -m venv ve
source ve/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

mkdir -p assets/qr-codes
mkdir _formatted_songs

deactivate
