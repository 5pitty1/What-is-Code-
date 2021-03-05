//
//  ContentView.swift
//  ViewsAndModifiers
//
//  Created by Michael Remediakis on 3/6/20.
//  Copyright © 2020 Mikeyopolis. All rights reserved.
//

import SwiftUI

struct ProminentTitle: ViewModifier {
    
    func body(content: Content) -> some View {
        content
            .font(.largeTitle)
            .foregroundColor(.blue)
    }
    
}

extension View {
    
    func prominentTitle() -> some View {
        self.modifier(ProminentTitle())
    }
}

struct ContentView: View {
    var body: some View {
        Text("Hello World!").prominentTitle()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
