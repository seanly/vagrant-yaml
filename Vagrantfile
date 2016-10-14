# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version ">= 1.6.0"
VAGRANTFILE_API_VERSION = "2"

require 'yaml'

`python parser.py`
yaml_ctx = YAML.load_file 'nodes.yaml'
machines = yaml_ctx['machines']

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
  machines.each do |machine|

    config.vm.define machine["name"] do |node|
      node.vm.box = machine["box"]
      node.vm.provider "virtualbox" do |vb|
          vb.memory = machine["mem"]
          vb.gui = machine['gui']
          if machine['cpus']
            vb.cpus = machine['cpus']
          end
      end

      private_network = machine['private_network']
      if private_network
        node.vm.network "private_network", ip: private_network['ip']
      end

      node.vm.hostname = machine['hostname']

      ssh = machine['ssh']
      if ssh
        node.ssh.username = ssh["username"]
        node.ssh.password = ssh["password"]
      end

      synced_folders = machine['synced_folders']
      synced_folders.each do |synced_folder|
        node.vm.synced_folder synced_folder['host'], synced_folder['guest']
      end
      shell = machine['shell']
      if shell
        node.vm.provision "shell", inline: shell
      end
    end
  end
end
