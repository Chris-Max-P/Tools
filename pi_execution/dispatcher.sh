# shellcheck disable=SC2164
if [[ "$1" == "-h" ]];
  then echo "eat, num, bank"
  exit 0
fi

cd /home/pi/Coding/Tools

case "$1" in
  eat)
    script="API.Rezepte.receipes"
    ;;
  num)
    script="API.Nummern.numbers"
    ;;
  bank)
    script="Finances.bin.get_account_balances_and_transactions"
    ;;
esac

python -m ${script}
