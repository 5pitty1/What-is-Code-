

let str = "b"
let num = Int(str)


struct Person {
    var id: String
    
    init?(id: String) {
        if id.count == 9 {
            self.id = id
        } else {
            return nil
        }
    }
}


let v = Person(id: "23456783")
