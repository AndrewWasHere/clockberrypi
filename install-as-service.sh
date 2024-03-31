#! /bin/bash
# Systemd service installation script.

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
SYSTEMD_USER_DIR="${HOME}/.config/systemd/user"
SERVICE="deskclock.service"

mkdir -p ${SYSTEMD_USER_DIR}
cp ${SCRIPT_DIR}/${SERVICE} ${SYSTEMD_USER_DIR}/${SERVICE}
systemctl --user daemon-reload
systemctl --user enable ${SERVICE}
echo "${SERVICE} is $(systemctl --user is-enabled ${SERVICE})"
loginctl enable-linger pi
