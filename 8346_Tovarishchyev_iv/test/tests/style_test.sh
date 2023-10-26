#!/bin/bash

sleep 1

if [ true ]
then
  ! pylint unit_code_pylint.py --enable C0301,E0401,W0401,C0410,E0602,R0903,W0212,R1735,C0209,C0411

  status=$?

  if [ $status -eq 0 ]
  then
    echo "Pylint: PASSED"
    exit 0
  else
    echo "Pylint: FAILED"
    exit 1
  fi
else
  echo "Pylint: DISABLED"
  exit 1
fi
