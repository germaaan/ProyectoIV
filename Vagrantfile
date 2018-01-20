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
    azure.tenant_id = 'c46110f5-71b3-4046-9bbf-fe08d2da884c'
    azure.client_id = '7f70283b-6fe7-4680-8373-9b4a352508c8'
    azure.client_secret = 'b40808e0-0c1d-4391-9140-56e0b9c4236e'
    azure.subscription_id = '3f568057-e917-40ca-9241-c76259749d53'    
  end

  config.vm.provision "ansible" do |ansible|
    ansible.become = true
    ansible.playbook = "./cve-play-book.yml"
    ansible.verbose = "v"
    ansible.host_key_checking = false
  end


end