#!/bin/bash

root=$(dirname $0)

sleep 1

if [ true ]
then
  ! black unit_code_pylint.py --check

  status=$?

  if [ $status -eq 0 ]
  then
    echo "Black: PASSED"
    exit 0
  else
    echo "Black: FAILED"
    exit 1
  fi
else
  echo "Black: DISABLED"
  exit 1
fi
