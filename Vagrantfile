# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version ">= 1.6.0"
VAGRANTFILE_API_VERSION = "2"

require 'yaml'

yaml_ctx = YAML.load_file 'nodes.yaml'
machines = yaml_ctx['machines']

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
  machines.each do |machine|

    config.vm.define machine['name'] do |node|
      node.vm.box = machine['box']
      node.vm.provider 'virtualbox' do |vb|
          if machine.include?('mem')
            vb.memory = machine['mem']
          end
          if machine.include?('gui')
            vb.gui = machine['gui']
          end
          if machine['cpus']
            vb.cpus = machine['cpus']
          end
      end

      private_network = machine['private_network']
      if private_network
        node.vm.network 'private_network', ip: private_network['ip']
      end

      forwarded_port = machine['forwarded_port']
      if forwarded_port
        config.vm.network 'forwarded_port', guest: forwarded_port['guest'], host: forwarded_port['host']
      end

      public_network = machine['public_network']
      if public_network
        if public_network.instance_of? Hash and public_network.include?('ip')
          config.vm.network 'public_network', ip: public_network['ip']
        else
          config.vm.network 'public_network'
        end
      end

      if machine.include?('hostname')
        node.vm.hostname = machine['hostname']
      end

      ssh = machine['ssh']
      if ssh
        node.ssh.username = ssh['username']
        node.ssh.password = ssh['password']
      end

      if machine.include?('synced_folders')
          synced_folders = machine['synced_folders']
          synced_folders.each do |synced_folder|
            node.vm.synced_folder synced_folder['host'], synced_folder['guest']
          end
      end
      shell = machine['shell']
      if shell
        node.vm.provision 'shell', inline: shell
      end
    end
  end
end
