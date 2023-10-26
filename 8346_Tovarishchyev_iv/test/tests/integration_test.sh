#!/bin/bash

sleep 1

if [ true ]

then
  python3 request.py

  status=$?

  if [ $status -eq 0 ]
  then
    echo "Integration: PASSED"
    exit 0
  else
    echo "Integration: FAILED"
    exit 1
  fi
else
  echo "Integration: DISABLED"
  exit 1
fi

