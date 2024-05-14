pm.test('Status cide is 200', function(){
    pm.response.to.have.status(200);
});




pm.test('Body matches string', function(){
    pm.expect(pm.response.text()).to.include("roomId");
});




pm.test("Response schema should match", function(){
    const schema={
        'properties':{
            "rooms": {"items": {
                "$id":"#/properties/rooms/items",
                "anyOf":[
                    {
                        "type": "object",
                        "required":["roomId", "floor", "guestNum", "beds", "price"],
                        "properties":{
                            "roomId":{"type": "integer"},
                            "floor":{"type": "integer"},
                            "guestNum":{"type": "integer"},
                            "beds":{"type": "integer"},
                            "price":{"type": "integer"}}}]}}}}

    pm.expect(tv4.validate(pm.response.json(), schema)).to.be.true
});

const rooms=pm.response.json().rooms

pm.environment.set("roomId", rooms[rooms.length-1].roomId)

pm.environment.set("roomRequest", pm.request)