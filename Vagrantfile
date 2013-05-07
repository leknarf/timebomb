# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "precise64"

  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  config.vm.box_url = "https://s3.amazonaws.com/gsc-vagrant-boxes/ubuntu-12.04.2-i386-chef-11-omnibus.box"

  # Forward port 8080 on the host machine to port 80 on the VM
  config.vm.network :forwarded_port, guest:80, host: 8080

  # Enable berkshelf integration
  config.berkshelf.enabled = true
  config.berkshelf.berksfile_path = "../timebomb-chef/Berksfile"

  # Enable provisioning with chef solo, specifying a cookbooks path, roles
  # path, and data_bags path (all relative to this Vagrantfile), and adding
  # some recipes and/or roles.
  config.vm.provision :chef_solo do |chef|
    chef.cookbooks_path = "../timebomb-chef/private_cookbooks"
    chef.add_recipe "timebomb::timebomb_app"
  end
end
