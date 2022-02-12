# shellcheck disable=SC2164
if [[ "$1" == "-h" ]];
  then echo "eat, num, bank"
  exit 0
fi

cd /home/pi/Coding/Tools

case "$1" in
  eat)
    py_mode="-c"
    script="from API.receipes import output_receipe; output_receipe()"
    ;;
  num)
    py_mode="-m"
    script=$'\'API.numbers\''
    ;;
  bank)
    py_mode="-m"
    script="Finances.bin.get_account_balances_and_transactions"
    ;;
esac

python ${py_mode} ${script}
