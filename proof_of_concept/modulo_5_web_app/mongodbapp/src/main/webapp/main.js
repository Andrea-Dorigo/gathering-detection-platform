new Vue({
    el: "#slider",
    data() {
        return {
            value: ""
        }
    },
    methods: {
        setColor: function() {
            if (this.value > 0) {
                return {
                    color: "#black",
                }

            }
        }
    },
});

new Vue({
        el: '#datepicker',
        data: {
          selectedDate: null,
        }
})
