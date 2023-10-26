#!/bin/bash

sleep 1

if [ true ]
then
  python3 selenium_test.py

  status=$?

  if [ $status -eq 0 ]
  then
    echo "Selenium: PASSED"
    exit 0
  else
    echo "Selenium: FAILED"
    exit 1
  fi
else
  echo "Selenium: DISABLED"
  exit 1
fi
