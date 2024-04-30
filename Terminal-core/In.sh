function ins {
  echo $1 > /storage/emulated/0/MYC/_connected_fmyc.od
  echo "MYC"
  echo "VERSION 1.0"
  echo -e "\033[32m ECHO OUTPUT: "
  python /storage/emulated/0/MYC/Build.py
  echo -e "\033[0m FS "
}
