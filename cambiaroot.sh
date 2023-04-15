#!/bin/bash
echo "ingrese el nombre del archivo a cambiar a root"
read archivo
chmod +x $archivo
sudo chown root $archivo
