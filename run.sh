#!/bin/bash
for i in {90..9092}
do
gnome-terminal --tab -- sh -c " cd /home/altaiim/PycharmProjects/translate/exacute; python3 test${i}.py; bash"
               done