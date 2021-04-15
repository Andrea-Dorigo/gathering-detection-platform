import { mount, /*shallowMount*/ } from "@vue/test-utils"
import chiSiamo from "../../components/chiSiamo.vue"
import autocompleteSearch from '../../components/autocompleteSearch.vue'
//import basicExample from '../../components/BasicExample.vue'
//import slider2 from '../../components/slider2.vue'
//import datePicker from '../../components/datePicker.vue'

describe("chiSiamo", () => {
  const wrapper = mount(chiSiamo);
  test('should check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  })
})

describe("autocompleteSearch", () => {
  const wrapper = mount(autocompleteSearch);
  test('should check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  })
  test('should check if search bar is empty', () => {
    expect(wrapper.find('input').text()).toBe('');
  })
})

/*describe("basicExample", () => {
  const wrapper = shallowMount(basicExample);
  test('should check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  })
})*/