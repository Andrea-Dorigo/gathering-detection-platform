import { mount } from "@vue/test-utils"
import chiSiamo from "../../components/chiSiamo.vue"

describe("chiSiamo", () => {
  const wrapper = mount(chiSiamo);
  test('should check if exist', () =>{
    expect(wrapper.exists()).toBe(true);
    expect(wrapper.find('does-not-exist').exists()).toBe(false);
    expect(wrapper.find("h1").exists()).toBe(true);
  })
})