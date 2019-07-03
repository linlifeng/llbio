history | tail -n1 | tr -s ' ' | sed -e 's/^ //' | cut -f2- -d ' ' | sed -e 's/| bank.sh//g' >> commands.sh
