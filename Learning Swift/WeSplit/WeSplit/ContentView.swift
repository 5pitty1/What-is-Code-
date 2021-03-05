//
//  ContentView.swift
//  WeSplit
//
//  Created by Michael Remediakis on 2/29/20.
//  Copyright © 2020 Mikeyopolis. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    @State private var checkCost = ""
    @State private var numSharing = ""
    @State private var tipPercent = 2
    
    let tipPercentages = [10, 15, 20, 25, 0]
    
    var totalAfterTip: Double {
        let tipSelection = Double(tipPercentages[tipPercent])
        let orderAmount = Double(checkCost) ?? 0
        
        return orderAmount*(1+0.01*tipSelection)
    }
    var totalPerPerson: Double {
        let peopleCount = Double(numSharing) ?? 1
        
        return totalAfterTip/(peopleCount)
    }
    
    var body: some View {
        NavigationView {
            Form {
                Section {
                    TextField("Amount", text: $checkCost)
                        .keyboardType(.decimalPad)
                    TextField("Number of People", text: $numSharing)
                        .keyboardType(.numberPad)
                }
                Section(header: Text("How much tip do you want to leave?")) {
                    Picker("Tip percentage", selection: $tipPercent) {
                        ForEach(0 ..< tipPercentages.count) { i in
                            Text("\(self.tipPercentages[i])%")
                        }
                    }.pickerStyle(SegmentedPickerStyle())
                }
                Section(header: Text("Check after tip")) {
                    Text("$\(totalAfterTip, specifier: "%.2f")")
                }
                Section(header: Text("Amount per person")) {
                    Text("$\(totalPerPerson, specifier: "%.2f")")
                        .foregroundColor(tipPercent == 4 ? .red : .black)
                }
            }.navigationBarTitle("WeSplit")
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
