import { mount} from "@vue/test-utils"
import chiSiamo from "../../components/aboutUs.vue"
import autocompleteSearch from '../../components/autocompleteSearch.vue'
import heatMap from '../../components/heatMap.vue'
import slider from '../../components/slider.vue'
import datePicker from '../../components/datePicker.vue'
import listCity from '../../components/listCity.vue'
import mainPage from '../../components/mainPage.vue'
import vue2LeafletHeatmap from '../../components/vue2LeafletHeatmap.vue'
import App from '../../App.vue'

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
  test('user shuold have written something', () => {
    expect(wrapper.find('input').trigger('keyup')).not.toBe('');
  })
  test('the get shuold work', () =>{
    expect(wrapper.vm.getNameCity).not.toBe(null);
  })
})

describe("datePicker", () => {
  const wrapper = mount(datePicker);
  test('should check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  })
})

describe("slider", () => {
  const wrapper = mount(slider);
  test('should check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  })
})


describe("App", () => {
  const wrapper = mount(App);
  test('should check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  })
})

describe("listCity", () => {
  const wrapper = mount(listCity);
  test('should check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  })
})

describe("vue2LeafletHeatmap", () => {
  const wrapper = mount(vue2LeafletHeatmap);
  test('should check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  })
})

describe("heatMap", () => {
  const wrapper = mount(heatMap);
  test('should check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  })
})

describe("mainPage", () => {
  const wrapper = mount(mainPage);
  test('should check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  })
})