# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure('2') do |config|

  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'
  config.vm.network "private_network",ip: "192.168.11.4", virtualbox__intnet: "vboxnet0"
  config.vm.hostname = "localhost"
  config.vm.network "forwarded_port", guest: 80, host: 80

  # use local ssh key to connect to remote vagrant box
  config.vm.provider :azure do |azure, override|

    config.ssh.private_key_path = '~/.ssh/id_rsa'

    azure.vm_image_urn = 'canonical:UbuntuServer:16.04-LTS:16.04.201701130'
    azure.vm_size = 'Basic_A0'
    azure.location = "westeurope"
    azure.tcp_endpoints = '80'
    azure.vm_name = "basecve"
    azure.resource_group_name= "recursosiv"

    #Identificación servicio en Azure
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']
   
  end

  config.vm.provision "ansible" do |ansible|
    ansible.become = true
    ansible.playbook = "./cve-play-book.yml"
    ansible.verbose = "v"
    ansible.host_key_checking = false
  end


end
