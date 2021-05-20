/*jshint esversion: 6 */
import { mount, shallowMount} from "@vue/test-utils";
import chiSiamo from "../../components/aboutUs.vue";
import autocompleteSearch from '../../components/autocompleteSearch.vue';
import heatMap from '../../components/heatMap.vue';
import slider from '../../components/slider.vue';
import datePicker from '../../components/datePicker.vue';
import listCity from '../../components/listCity.vue';
import mainPage from '../../components/mainPage.vue';
import vue2LeafletHeatmap from '../../components/vue2LeafletHeatmap.vue';
import App from '../../App.vue';
import httpRequest from '../../services/htpprequest.js';
import httpcommon from '../../http-common.js';
import confrontoCittà from '../../components/confrontoCittà.vue'

describe("chiSiamo", () => {
  const wrapper = mount(chiSiamo);
  test('check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  });
});

describe("confrontoCittà", () => {
  const wrapper = mount(confrontoCittà);
  test('check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  });
});


describe("httpcommon", () => {
  const wrapper = mount(httpcommon);
  test('check if exist', () => {
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  });
});

describe("httpRequest", () => {
  const wrapper = mount(httpRequest);
  test('check if getCities work', () =>{
    expect(wrapper.vm.getCities).not.toBe(null);
  });
  test('check if getCoo work', () =>{
    expect(wrapper.vm.getCoo).not.toBe(null);
  });
  test('check if getDataRT work', () =>{
    expect(wrapper.vm.getDataRT).not.toBe(null);
  });
  test('check if getLastValue work', () =>{
    expect(wrapper.vm.getLastValue).not.toBe(null);
  });
});

describe("autocompleteSearch", () => {
  const wrapper = mount(autocompleteSearch);
  test('check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  });
  test('check if search bar is empty', () => {
    expect(wrapper.find('input').text()).toBe('');
  });
  test('user should have written something', () => {
    expect(wrapper.find('input').trigger('keyup')).not.toBe('');
  });
  test('check if the get work', () =>{
    expect(wrapper.vm.getNameCity).not.toBe(null);
  });
  test('check if the get is called', () =>{
    const mockGet = jest.spyOn(wrapper.vm, "getNameCity");
    expect(mockGet).not.toBe(null);
  });
  test('check if the itemSelected work', () =>{
    expect(wrapper.vm.itemSelected).not.toBe(null);
  });
});

describe("datePicker", () => {
  const wrapper = shallowMount(datePicker);
  test('check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  });
});

describe("slider", () => {
  const wrapper = mount(slider);
  test('check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  });
  test('the get should work', () =>{
    expect(wrapper.vm.getTime).not.toBe(null);
  });
});


describe("App", () => {
  const wrapper = mount(App);
  test('check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  });
});

describe("listCity", () => {
  const wrapper = mount(listCity);
  test('check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  });
});

describe("vue2LeafletHeatmap", () => {
  const wrapper = shallowMount(vue2LeafletHeatmap);
  test('check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  });
});

describe("heatMap", () => {
  const wrapper = shallowMount(heatMap);
  test('check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  });
});

describe("mainPage", () => {
  const wrapper = shallowMount(mainPage);
  test('check if component heatmap exixst', () => {
    expect(wrapper.findComponent(heatMap).exists()).toBe(true);
  });
  test('check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
  });
});