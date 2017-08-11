package com.restlesschimp;

public class Phone {
    String model;
    String company;
    Phone(String model) {
        this.model = model;
    }
    double weight;
    void makeCall(String number) {
        System.out.println("making call");
    }
    void receiveCall() {
        System.out.println("receiving call");
    }
}
