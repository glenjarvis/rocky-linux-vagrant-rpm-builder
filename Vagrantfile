# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/8"

  config.vm.provider "virtualbox" do |v|
    v.name = "rocky-linux-rpm-tester"
  end

  config.vm.provision "shell" do |p|
    p.inline = "/vagrant/setup.sh"
  end
end
