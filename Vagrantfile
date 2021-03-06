# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version ">= 1.6.0"
VAGRANTFILE_API_VERSION = "2"

require 'yaml'

yaml_ctx = YAML.load_file(File.join(File.dirname(__FILE__), 'hosts.yml'))
machines = yaml_ctx['machines']

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
  machines.each do |machine|

    config.vm.define machine['name'] do |node|
      node.vm.box = machine['box']
      node.vm.box_check_update = false
      node.vm.provider 'virtualbox' do |vb|
      node.vm.boot_timeout = 120
        if machine.include?('gui')
          vb.gui = machine['gui']
        else
          vb.gui = false
        end
        if machine['cpus']
          vb.cpus = machine['cpus']
        else
          vb.cpus = 2
        end
        if machine.include?('mem')
          vb.memory = machine['mem']
        else
          vb.memory = 2048
        end
        if machine.include?('controller')
          data_disk = ".disk/#{machine['name']}-data.vdi"
          controller = machine['controller']
          if ARGV[0] == "up"
            if ! File.exist?(data_disk)
              vb.customize [
                'createhd', 
                '--filename', data_disk, 
                '--format', 'VDI', 
                '--size', 10 * 1024 # 10 GB
              ] 
            end
            vb.customize [
              'storageattach', :id, 
              '--storagectl', controller, 
              '--port', 2, '--device', 0, 
              '--type', 'hdd', '--medium', 
              data_disk
            ]
          end
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
      else
        node.vm.hostname = machine['name']
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
