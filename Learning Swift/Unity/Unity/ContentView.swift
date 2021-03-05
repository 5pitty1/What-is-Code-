//
//  ContentView.swift
//  Unity
//
//  Created by Michael Remediakis on 3/4/20.
//  Copyright © 2020 Mikeyopolis. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    @State private var userInput = ""
    @State private var userUnit = 0
    @State private var outputUnit = 0
    
    var unitOptions = ["Meters", "Feet", "Yard", "Miles"]
    var conversionRate = [1.0, 3.28084, 1.09361, 0.000621371]

    var output:Double {
        let userInputVal = Double(userInput) ?? 0
        
        let baseline = userInputVal/conversionRate[userUnit]
        
        return baseline * conversionRate[outputUnit]
    }
    
    var body: some View {
        NavigationView {
            Form {
                Section {
                    TextField("Input Value", text: $userInput)
                }
                
                Section(header: Text("What units do you want to convert between?")) {
                    Picker("Input Units", selection: $userUnit) {
                        ForEach(0..<unitOptions.count) {
                            Text("\(self.unitOptions[$0])")
                        }
                    }.pickerStyle(SegmentedPickerStyle())

                    Picker("Units", selection: $outputUnit) {
                        ForEach(0..<unitOptions.count) {
                            Text("\(self.unitOptions[$0])")
                        }
                    }.pickerStyle(SegmentedPickerStyle())
                }
                
                Section {
                    Text("\(output, specifier: "%g") \(unitOptions[outputUnit])")
                }
            }.navigationBarTitle("Unity")
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
