#! /usr/bin/env python3.5
# -*- coding: utf-8 -*-
import paramiko


class RunCommandSSH:
    """
    Simple shell to run a command on the host
    """

    def __init__(self, host, username, password, port):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.sudo_password = password
        self.connections = None

    def _do_connect(self):
        """
        Connect to host
        """
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host,
                       username=self.username,
                       password=self.password,
                       port=self.port)
        self.connections = client

    def _close(self):
        self.connections.close()

    def run(self, command):
        """
        Execute command on host
        :return stdout of command
        """
        self._do_connect()
        stdin, stdout, stderr = self.connections.exec_command(command, get_pty=True)
        data = stdout.read().split()
        stdin.close()
        self._close()
        return data

    def put_by_ftp(self, local_path, remote_path):
        """
        Put file on host
        """
        self._do_connect()
        ftp = self.connections.open_sftp()
        ftp.put(local_path, remote_path)
        ftp.close()
        self._close()

    def get_by_ftp(self, remote_path, local_path):
        """
        Get file from host
        """
        self._do_connect()
        ftp = self.connections.open_sftp()
        ftp.get(remote_path, local_path)
        ftp.close()
        self._close()

    def service_restart(self, service):
        """
        Restart service
        """
        command = 'service {} restart'.format(service)
        self.run(command)

    def service_status_check(self, service):
        """
        Check service status
        """
        command = 'service --status-all | grep {} '.format(service)
        data = self.run(command)
        if data[1] != b'+':
            raise ValueError("{} service status is {}".format(service, data[1]))
